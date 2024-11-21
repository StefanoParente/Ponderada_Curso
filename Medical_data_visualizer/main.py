from medical_data_visualizer import draw_cat_plot, draw_heat_map

cat_plot_figure = draw_cat_plot()
cat_plot_figure.savefig('catplot.png')

heat_map_figure = draw_heat_map()
heat_map_figure.savefig('heatmap.png')
