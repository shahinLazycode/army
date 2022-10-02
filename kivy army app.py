from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty

import csv


class Score:
    def __init__(self, age:int, record:int) -> None:
        # meghdar dehi avali property
        self.record = record
        self.age = age
        return None

    def find_score_with_record(self, title:str) -> int:
        with open(f'{title}.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for index, row in enumerate(reader):
                if index == 0:
                    record_title = self.find_age_title(row)
                
                if index == 0 and int(row[record_title]) <= self.record:
                    return int(row['score'])
                elif int(row[record_title]) == self.record:
                    return int(row['score'])

    def find_age_title(self, row:dict) -> int:
        for title in row:
            try:
                age_title = title.split('-')
                age_title = list(map(int, age_title))
                if age_title[0] <= self.age <= age_title[1]:
                    return title
            except ValueError:
                pass

Builder.load_file('army.kv')

class MyLayout(Widget):
    def press(self):
        age = int(self.ids.sen.text)
        enetaf = int(self.ids.enetaf.text)
        find_score = Score(age, enetaf)
        self.ids.enetaf_score.text = str(find_score.find_score_with_record('flexibilty'))

class ArmyApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    ArmyApp().run()