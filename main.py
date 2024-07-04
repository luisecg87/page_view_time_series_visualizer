from page_view_time_series_visualizer import load_and_clean_data, draw_line_plot, draw_bar_plot, draw_box_plot

# Cargar y limpiar los datos
file_path = 'fcc-forum-pageviews.csv'  # Asegúrate de tener el archivo en el mismo directorio
df = load_and_clean_data(file_path)

# Generar y guardar los gráficos
line_plot_fig = draw_line_plot(df)
bar_plot_fig = draw_bar_plot(df)
box_plot_fig = draw_box_plot(df)
