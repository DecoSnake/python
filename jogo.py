import random
import time
from IPython.display import clear_output
from google.colab import output

# Game parameters
board_size = 10
snake = [(board_size // 2, board_size // 2)]
food = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
# direction = 'RIGHT' # We will now control direction with keys
score = 0

# Store the current direction based on key presses
current_direction = 'RIGHT'

def create_food():
    while True:
        f = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
        if f not in snake:
            return f

def move_snake():
    global snake, food, current_direction, score

    head_x, head_y = snake[0]

    if current_direction == 'UP':
        new_head = (head_x, head_y - 1)
    elif current_direction == 'DOWN':
        new_head = (head_x, head_y + 1)
    elif current_direction == 'LEFT':
        new_head = (head_x - 1, head_y)
    elif current_direction == 'RIGHT':
        new_head = (head_x + 1, head_y)

    # Check for collision with walls or self
    if (new_head in snake or
        not (0 <= new_head[0] < board_size and 0 <= new_head[1] < board_size)):
        print("Game Over!")
        print(f"Final Score: {score}")
        # Reset game
        snake = [(board_size // 2, board_size // 2)]
        food = create_food()
        current_direction = 'RIGHT'
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

# Function to handle keyboard input
def on_key_event(event):
    global current_direction
    if event['key'] == 'ArrowUp' and current_direction != 'DOWN':
        current_direction = 'UP'
    elif event['key'] == 'ArrowDown' and current_direction != 'UP':
        current_direction = 'DOWN'
    elif event['key'] == 'ArrowLeft' and current_direction != 'RIGHT':
        current_direction = 'LEFT'
    elif event['key'] == 'ArrowRight' and current_direction != 'LEFT':
        current_direction = 'RIGHT'

# Register keyboard event listener
output.register_keyboard_handler(on_key_event)


# Game loop
print("Starting Snake Game (text-based, use arrow keys)...")
time.sleep(1)

game_on = True
while game_on:
    draw_board()
    game_on = move_snake()
    time.sleep(0.3) # Adjust speed here

# Unregister keyboard handler when the game loop ends
output.unregister_keyboard_handler()
