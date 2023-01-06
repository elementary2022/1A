from random import randint

z = [[randint(0, 10) for y in range(2)] for x in range(100)]
alpha = [z[x: x + 5] for x in range(0, len(z), 5)]
for y in alpha:
    print('{} + {} &= \\underline{{\hspace{{1cm}}}} & {} + {} &= \\underline{{\hspace{{1cm}}}} & {} + {} &= \\underline{{\hspace{{1cm}}}} & {} + {} &= \\underline{{\hspace{{1cm}}}} & {} + {} &= \\underline{{\hspace{{1cm}}}} \\\\'.format(
        y[0][0], y[0][1], y[1][0], y[1][1], y[2][0], y[2][1], y[3][0], y[3][1], y[4][0], y[4][1]))
print('-' * 80)
print('-' * 80)
for y in alpha:
    print('{} + {} &= {} & {} + {} &= {} & {} + {} &= {} & {} + {} &= {} & {} + {} &= {} \\\\'.format(
        y[0][0], y[0][1], y[0][0] + y[0][1], y[1][0], y[1][1], y[1][0] + y[1][1], y[2][0], y[2][1], y[2][0] + y[2][1], y[3][0], y[3][1], y[3][0] + y[3][1], y[4][0], y[4][1], y[4][0] + y[4][1]))
