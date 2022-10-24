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
        if self.record == 0:
            with open(f'{title}.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if index == 0:
                        record_title = self.find_age_title(row)
                    if index == 0 and int(row[record_title]) <= self.record:
                        return int(row['score'])
                    elif int(row[record_title]) == self.record:
                        return int(row['score'])
        else:
            return 0
    
    def find_score_with_record_time(self, title:str) -> float:
        if self.record == 0:
            with open(f'{title}.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    if index == 0:
                        record_title = self.find_age_title(row)
                    if index == 0 and float(row[record_title]) >= self.record:
                        return int(row['score'])
                    elif float(row[record_title]) == self.record:
                        return int(row['score'])
        else:
            return 0

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
        try:
            age = int(self.ids.sen.text)
        except ValueError:
            age = 0
        
        try:
            shena = int(self.ids.shena.text)
        except ValueError:
            shena = 0
        find_shena_score = Score(age, shena)
        self.ids.shena_score.text = str(find_shena_score.find_score_with_record('shena'))
            
        try:
            barfix = int(self.ids.barfix.text)
        except ValueError:
            barfix = 0
        find_barfix_score = Score(age, barfix)
        self.ids.barfix_score.text = str(find_barfix_score.find_score_with_record('barfix'))
            
        try:
            derazneshast = int(self.ids.derazneshast.text)
        except ValueError:
            derazneshast = 0
        find_derazneshast_score = Score(age, derazneshast)
        self.ids.derazneshast_score.text = str(find_derazneshast_score.find_score_with_record('derazneshast'))
            
        try:
            enetaf = int(self.ids.enetaf.text)
        except ValueError:
            enetaf = 0
        find_enetaf_score = Score(age, enetaf)
        self.ids.enetaf_score.text = str(find_enetaf_score.find_score_with_record('enetaf'))
            
        try:
            agility = float(self.ids.agility.text)
        except ValueError:
            agility = 0
        find_agility_score = Score(age, agility)
        self.ids.agility_score.text = str(find_agility_score.find_score_with_record_time('agility'))

        try:
            speed = float(self.ids.speed.text)
        except ValueError:
            speed = 0
        find_speed_score = Score(age, speed)
        self.ids.speed_score.text = str(find_speed_score.find_score_with_record_time('speed'))

        try:
            stamina = float(self.ids.stamina.text)
        except ValueError:
            stamina = 0
        find_stamina_score = Score(age, stamina)
        self.ids.stamina_score.text = str(find_stamina_score.find_score_with_record_time('stamina'))
    
    def clear(self):
        self.ids.shena.text==0
        

        
class ArmyApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    ArmyApp().run()