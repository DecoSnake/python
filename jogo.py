import streamlit as st
import random

# Inicializa estado da sessão
if 'snake' not in st.session_state:
    st.session_state.snake = [(5, 5)]
    st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    st.session_state.direction = 'RIGHT'
    st.session_state.score = 0

# Função para mover a minhoca
def move_snake():
    head_x, head_y = st.session_state.snake[0]
    if st.session_state.direction == 'UP':
        new_head = (head_x, head_y - 1)
    elif st.session_state.direction == 'DOWN':
        new_head = (head_x, head_y + 1)
    elif st.session_state.direction == 'LEFT':
        new_head = (head_x - 1, head_y)
    else:  # RIGHT
        new_head = (head_x + 1, head_y)

    # Verifica colisão
    if (new_head in st.session_state.snake or
        not (0 <= new_head[0] < 10 and 0 <= new_head[1] < 10)):
        st.session_state.snake = [(5, 5)]
        st.session_state.direction = 'RIGHT'
        st.session_state.score = 0
        st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
    else:
        st.session_state.snake.insert(0, new_head)
        # Verifica se comeu a comida
        if new_head == st.session_state.food:
            st.session_state.score += 1
            st.session_state.food = (random.randint(0, 9), random.randint(0, 9))
        else:
            st.session_state.snake.pop()

# Streamlit UI
st.title("Snake Game")

# Botões de direção
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("UP"):
        if st.session_state.direction != 'DOWN':
            st.session_state.direction = 'UP'
with col1:
    if st.button("LEFT"):
        if st.session_state.direction != 'RIGHT':
            st.session_state.direction = 'LEFT'
with col3:
    if st.button("RIGHT"):
        if st.session_state.direction != 'LEFT':
            st.session_state.direction = 'RIGHT'
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("DOWN"):
        if st.session_state.direction != 'UP':
            st.session_state.direction = 'DOWN'

# Mover a minhoca em cada atualização
move_snake()

# Desenha o tabuleiro
board_size = 10
for y in range(board_size):
    row = ""
    for x in range(board_size):
        if (x, y) in st.session_state.snake:
            row += "🟢"
        elif (x, y) == st.session_state.food:
            row += "🍎"
        else:
            row += "⬜"
    st.markdown(row)

st.write(f"Score: {st.session_state.score}")

# Auto-refresh (para animação básica, pode não ser ideal para jogos rápidos)
# import time
# time.sleep(0.5)
# st.experimental_rerun()
