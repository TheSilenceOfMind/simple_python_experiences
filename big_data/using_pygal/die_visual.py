import pygal

from using_pygal.die import Die

# create 2 D6 dice
die_1 = Die()
die_2 = Die(10)

# do rolls, save statistics
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the result
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    i = results.count(value)
    frequencies.append(i)

# visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling D6 and D10 dice 50000 times"
hist.x_labels = list(range(2, max_result+1))
hist.x_title = 'result'
hist.y_title = 'frequency of result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')
