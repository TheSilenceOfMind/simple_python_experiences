import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS, Style

# Make an API call and store the result
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)

# store API result in variable
response_dict = r.json()
print('Total repositories: ', response_dict['total_count'])

# explore info about repos
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    if plot_dict['label'] == None:
        plot_dict['label'] = ''
    plot_dicts.append(plot_dict)

# make visualisation
my_style = LS('#333366', base_style=LCS, tooltip_font_size=10)

# set config for bar chart
cfg = pygal.Config()
cfg.x_label_rotation = 45
cfg.show_legend = False
cfg.title_font_size = 24
cfg.label_font_size = 14
cfg.major_label_font_size = 18
cfg.truncate_label = 15
cfg.show_y_guides = False
cfg.width = 1000
cfg.height = 450

chart = pygal.Bar(cfg, style=my_style)
chart.title = 'Most-starred python repos on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_in_browser()
