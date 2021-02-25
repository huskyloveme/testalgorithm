x = int(input('enter integer x: '))
y = int(input('enter integer y: '))


def find_nb_step(x, y):
    nb_step = 0
    logs = ''
    while True:
        if x == y:
            return nb_step, logs
        if y < x:
            y += 1
            logs = '-' + logs
            nb_step += 1
        elif y % 2 == 1:
            y += 1
            logs = '-' + logs
            y /= 2
            logs = '*' + logs
            nb_step += 2
        else:
            y /= 2
            logs = '*' + logs
            nb_step += 1


nb_step, logs = find_nb_step(x, y)
print('nb_step', nb_step)
print('logs', logs)
