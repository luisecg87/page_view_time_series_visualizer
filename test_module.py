import unittest
import pandas as pd
from page_view_time_series_visualizer import load_and_clean_data, draw_line_plot, draw_bar_plot, draw_box_plot

class PageViewTimeSeriesVisualizerTestCase(unittest.TestCase):
    def setUp(self):
        self.file_path = 'fcc-forum-pageviews.csv'
        self.df = load_and_clean_data(self.file_path)

    def test_load_and_clean_data(self):
        df = load_and_clean_data(self.file_path)
        self.assertEqual(df.shape[1], 1)  # Verificar que solo hay una columna 'value'

    def test_draw_line_plot(self):
        fig = draw_line_plot(self.df)
        self.assertIsNotNone(fig)

    def test_draw_bar_plot(self):
        fig = draw_bar_plot(self.df)
        self.assertIsNotNone(fig)

    def test_draw_box_plot(self):
        fig = draw_box_plot(self.df)
        self.assertIsNotNone(fig)

if __name__ == '__main__':
    unittest.main()
