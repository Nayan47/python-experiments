updown = 0
leftright = 0
while True:
    dir_step = input("direction steps: ")
    if not dir_step:
        break;
    dir_step = dir_step.split(' ')
    direction = dir_step[0].upper()
    step = int(dir_step[1])

    if direction == "UP":
        updown = updown + step
    elif direction == "DOWN" :
        updown = updown - step
    elif direction == "LEFT":
        leftright = leftright - step
    elif direction == "RIGHT":
        leftright = leftright + step

print(f"Distance: {int((updown**2+leftright**2)**(1/2))}")