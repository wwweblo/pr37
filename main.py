# main.py

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.colorpicker import ColorPicker


class PaintWidget(Widget):
    def __init__(self, **kwargs):
        super(PaintWidget, self).__init__(**kwargs)
        self.current_color = (1, 0, 0, 1)  # Default color is red

    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.current_color)
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def set_color(self, color):
        self.current_color = color


class PaintApp(App):
    def build(self):
        layout = FloatLayout()

        # Create the paint widget
        self.paint_widget = PaintWidget(size_hint=(1, 0.8))

        # Create the clear button
        clear_btn = Button(text='Clear', size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0})
        clear_btn.bind(on_release=self.clear_canvas)

        # Create the title label
        title = Label(text='Kivy Paint Application', size_hint=(1, 0.1), pos_hint={'x': 0, 'y': 0.9})

        # Create the color picker
        self.color_picker = ColorPicker(size_hint=(0.8, 0.2), pos_hint={'x': 0.2, 'y': 0})
        self.color_picker.bind(color=self.on_color)

        # Add the widgets to the layout
        layout.add_widget(self.paint_widget)
        layout.add_widget(clear_btn)
        layout.add_widget(title)
        layout.add_widget(self.color_picker)

        return layout

    def clear_canvas(self, instance):
        self.paint_widget.canvas.clear()

    def on_color(self, instance, value):
        self.paint_widget.set_color(value)


if __name__ == '__main__':
    PaintApp().run()
