html_code = """
<canvas id="pongCanvas" width="600" height="400" style="border:1px solid #000;"></canvas>

<script>
const canvas = document.getElementById('pongCanvas');
const ctx = canvas.getContext('2d');

// Game parameters
const PADDLE_WIDTH = 16;
const PADDLE_HEIGHT = 100;
const PADDLE_MARGIN = 24;
const BALL_RADIUS = 12;
const BALL_SPEED = 6;
const AI_SPEED = 4;

// Paddle positions
let leftPaddleY = (canvas.height - PADDLE_HEIGHT) / 2;
let rightPaddleY = (canvas.height - PADDLE_HEIGHT) / 2;

// Ball position and velocity
let ballX = canvas.width / 2;
let ballY = canvas.height / 2;
let ballVX = BALL_SPEED * (Math.random() > 0.5 ? 1 : -1);
let ballVY = BALL_SPEED * (Math.random() * 2 - 1);

// Scores
let leftScore = 0;
let rightScore = 0;

// Mouse control for left paddle
canvas.addEventListener('mousemove', function(e) {
    const rect = canvas.getBoundingClientRect();
    let mouseY = e.clientY - rect.top;
    leftPaddleY = mouseY - PADDLE_HEIGHT / 2;
    leftPaddleY = Math.max(0, Math.min(canvas.height - PADDLE_HEIGHT, leftPaddleY));
});

// Basic AI control for right paddle
function moveAIPaddle() {
    const targetY = ballY - PADDLE_HEIGHT / 2;
    if (rightPaddleY + PADDLE_HEIGHT / 2 < targetY) {
        rightPaddleY += AI_SPEED;
    } else if (rightPaddleY + PADDLE_HEIGHT / 2 > targetY) {
        rightPaddleY -= AI_SPEED;
    }
    rightPaddleY = Math.max(0, Math.min(canvas.height - PADDLE_HEIGHT, rightPaddleY));
}

// Collision detection
function checkCollisions() {
    // Top/bottom wall
    if (ballY - BALL_RADIUS < 0) {
        ballY = BALL_RADIUS;
        ballVY *= -1;
    }
    if (ballY + BALL_RADIUS > canvas.height) {
        ballY = canvas.height - BALL_RADIUS;
        ballVY *= -1;
    }

    // Left paddle
    if (
        ballX - BALL_RADIUS < PADDLE_MARGIN + PADDLE_WIDTH &&
        ballY > leftPaddleY &&
        ballY < leftPaddleY + PADDLE_HEIGHT
    ) {
        ballX = PADDLE_MARGIN + PADDLE_WIDTH + BALL_RADIUS;
        ballVX *= -1.1;
        ballVY += (ballY - (leftPaddleY + PADDLE_HEIGHT / 2)) * 0.1;
    }

    // Right paddle
    if (
        ballX + BALL_RADIUS > canvas.width - PADDLE_MARGIN - PADDLE_WIDTH &&
        ballY > rightPaddleY &&
        ballY < rightPaddleY + PADDLE_HEIGHT
    ) {
        ballX = canvas.width - PADDLE_MARGIN - PADDLE_WIDTH - BALL_RADIUS;
        ballVX *= -1.1;
        ballVY += (ballY - (rightPaddleY + PADDLE_HEIGHT / 2)) * 0.1;
    }

    // Left/right wall (score)
    if (ballX - BALL_RADIUS < 0) {
        rightScore++;
        resetBall(1);
    }
    if (ballX + BALL_RADIUS > canvas.width) {
        leftScore++;
        resetBall(-1);
    }
}

// Reset ball to center after a score
function resetBall(direction) {
    ballX = canvas.width / 2;
    ballY = canvas.height / 2;
    ballVX = BALL_SPEED * direction;
    ballVY = BALL_SPEED * (Math.random() * 2 - 1);
}

// Draw everything
function draw() {
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw net
    ctx.save();
    ctx.strokeStyle = '#555';
    ctx.lineWidth = 4;
    ctx.setLineDash([12, 16]);
    ctx.beginPath();
    ctx.moveTo(canvas.width / 2, 0);
    ctx.lineTo(canvas.width / 2, canvas.height);
    ctx.stroke();
    ctx.restore();

    // Draw paddles
    ctx.fillStyle = '#fff';
    ctx.fillRect(PADDLE_MARGIN, leftPaddleY, PADDLE_WIDTH, PADDLE_HEIGHT);
    ctx.fillRect(canvas.width - PADDLE_MARGIN - PADDLE_WIDTH, rightPaddleY, PADDLE_WIDTH, PADDLE_HEIGHT);

    // Draw ball
    ctx.beginPath();
    ctx.arc(ballX, ballY, BALL_RADIUS, 0, Math.PI * 2);
    ctx.fillStyle = '#fffb00';
    ctx.fill();

    // Draw score
    ctx.font = "48px monospace";
    ctx.fillStyle = "#fff";
    ctx.fillText(leftScore, canvas.width / 2 - 80, 60);
    ctx.fillText(rightScore, canvas.width / 2 + 40, 60);
}

// Main game loop
function update() {
    // Move ball
    ballX += ballVX;
    ballY += ballVY;

    moveAIPaddle();
    checkCollisions();
    draw();

    requestAnimationFrame(update);
}

// Start game
update();
</script>
"""

display(HTML(html_code))
