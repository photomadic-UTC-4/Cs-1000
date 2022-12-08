WIDTH = 820
HEIGHT = 765

board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'
game_over = False

def checkwin():
    for y in range(3):
        if board[y][0] == board[y][1] == board[y][2] and board[y][0] != ' ':
            win(board[y][0])
    for x in range(3):
        if board[0][x] == board[1][x] == board[2][x] and board[0][x] != ' ':
            win(board[0][x])
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        win(board[0][0])
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        win(board[0][2])

def win(player):
    global game_over, current_player
    game_over = True

def check_tie():
    for y in range(3):
        for x in range(3):
            if board[y][x] == ' ':
                return False
    return True

def draw():
    screen.fill((91, 206, 250))
    for y in range(3):
        for x in range(3):
            xpos = x * 260 + 10
            ypos = y * 255 + 10
            rect = Rect(xpos, ypos, 240, 235)
            screen.draw.filled_rect(rect, (245, 245, 245))
            text = board[y][x]
            screen.draw.text(text, (xpos + 120, ypos + 117), fontsize=60, color=(245, 169, 184))
    if game_over:
        text = f"Player {current_player} wins!"
        if check_tie():
            text = "It's a cat!"
        screen.draw.text(text, (WIDTH // 2, HEIGHT // 2), fontsize=40, color=(255, 0, 0), anchor=(0.5, 0.5))

def on_mouse_down(pos):
    global current_player, game_over
    x = pos[0] // 260
    y = pos[1] // 255
    if game_over or board[y][x] != ' ':
        return
    board[y][x] = current_player
    checkwin()
    if check_tie():
        game_over = True
    else:
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
