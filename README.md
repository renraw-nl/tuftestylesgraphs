# Tufte Styled Graphs

Matplotlib graphs using styles inspired by Tufte's principles in 'The Visual Display of Quantitative Information'.

Note it is a hobby project, things will vary and change.

## Inspirations and Sources

1. [Tufte](https://www.edwardtufte.com/tufte/)
2. Python packages [tufte](https://pypi.org/project/tufte/) and [juanshishido/tufte](https://github.com/juanshishido/tufte)
3. Pandas method chaining ([example](https://towardsdatascience.com/using-pandas-method-chaining-to-improve-code-readability-d8517c5626ac))
4. Matplotlib's [Parts of a Figure](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#parts-of-a-figure)
5. "Storytelling with data" by Cole Nussbaumer Knaflic ([charts](https://www.storytellingwithdata.com/chart-guide))

## Interface

Idea is to chain link method calls leading to something along the lines of:
``` python
(
    ScatterGraph()
     .add(group_names, group_data)
     .rotate_labels()
     .show_values(fmt="{:.1f}")
     .draw()
)
```

Idea is to select a graph type, feed it the data, adjust a few (limited) items and draw or save the graph. By default
the graph object should set the basics, such as:

1. Set the x and y axes,
2. Length of the spines and ticks,
3. Colors, font type and size.

## Working on

Basics:

1. Scatter graphs,
2. Line graphs,
3. Horizontal and Vertical Bar graphs,

And later on:

4. [Heatmap](https://github.com/BindiChen/machine-learning/blob/main/data-analysis/007-method-chaining/method-chaining.ipynb)
5. Sloped graphs ([Tufte's example](https://www.edwardtufte.com/bboard/q-and-a-fetch-msg?msg_id=0003nk), [Storytelling example](https://www.storytellingwithdata.com/blog/2020/7/27/what-is-a-slopegraph))
6. Highlights, or dimmed data.

### Others

1. Tests,
2. Typing,
3. Docs.

## Relation to Tufte and "Storytelling with data"

There is none, other than an attempt to create an python module using `matplotlib` to produce graphs inspired by their ideas.

## License

Released under the MIT license. See [LICENSE](https://github.com/renraw-nl/tuftestyledgraphs/blob/main/LICENSE).
