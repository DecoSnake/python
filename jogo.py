# Game parameters
board_size = 10
snake = [(board_size // 2, board_size // 2)]
food = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
direction = 'RIGHT'
score = 0

def create_food():
    while True:
        f = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
        if f not in snake:
            return f

def move_snake():
    global snake, food, direction, score

    head_x, head_y = snake[0]

    if direction == 'UP':
        new_head = (head_x, head_y - 1)
    elif direction == 'DOWN':
        new_head = (head_x, head_y + 1)
    elif direction == 'LEFT':
        new_head = (head_x - 1, head_y)
    elif direction == 'RIGHT':
        new_head = (head_x + 1, head_y)

    # Check for collision with walls or self
    if (new_head in snake or
        not (0 <= new_head[0] < board_size and 0 <= new_head[1] < board_size)):
        print("Game Over!")
        print(f"Final Score: {score}")
        # Reset game
        snake = [(board_size // 2, board_size // 2)]
        food = create_food()
        direction = 'RIGHT'
        score = 0
        time.sleep(2) # Pause before restarting
        return False # Indicate game over

    snake.insert(0, new_head)

    # Check for food
    if new_head == food:
        score += 1
        food = create_food()
    else:
        snake.pop()

    return True # Indicate game is ongoing

def draw_board():
    clear_output(wait=True)
    for y in range(board_size):
        row = ""
        for x in range(board_size):
            if (x, y) in snake:
                row += "🟢"
            elif (x, y) == food:
                row += "🍎"
            else:
                row += "⬜"
        print(row)
    print(f"Score: {score}")

# Game loop
print("Starting Snake Game (text-based)...")
time.sleep(1)

game_on = True
while game_on:
    draw_board()
    game_on = move_snake()
    time.sleep(0.5) # Adjust speed here
