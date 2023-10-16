from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable

from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker

from datebase import History, engine




class Table(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        Session = sessionmaker(bind=engine)
        session_1 = Session()
        articles = session_1.query(History).filter(
            History.off_power.isnot(None),
            History.sw_off.isnot(None),
            History.sw_on.is_(None),
            ).order_by(desc(History.sw_off)).all()
        

        layout = BoxLayout(padding=0,)
        data_tables = MDDataTable(
            size_hint=(0.8, 0.9),
            column_data=[
                ("Column 1", dp(20)),
                ("Column 2", dp(30)),
                ("Column 3", dp(50), self.sort_on_col_3),
                ("Column 4", dp(30)),
                ("Column 5", dp(30)),
                ("Column 6", dp(30)),
                ("Column 7", dp(30), self.sort_on_col_2),],
            
            row_data=[
                # The number of elements must match the length
                # of the `column_data` list.
                (i.sw_off,i.sw,i.addres, i.sw_on,i.ups_live,i.sw_down_time,i.problem) for i in articles],
        )
        layout.add_widget(data_tables)
        return layout

    def sort_on_col_3(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][3]
            )
        )

    def sort_on_col_2(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: l[1][-1]
            )
        )