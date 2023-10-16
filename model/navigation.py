from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.datatables import MDDataTable

from .table import Table
class Example(MDApp):
    def build(self):
        data_table = MDDataTable(use_pagination=False,
            
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.9, 0.6),
            
            column_data=[
                ("Header 1", dp(30)),
                ("Header 2", dp(30)),
                # Добавьте столбцы, какие вам нужны
            ],
            
            row_data=[
                ("Data 1", "Data 2"),
                ("Data 3", "Data 4"),
                # Добавьте данные, какие вам нужны
            ],
        )
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        return (
            MDScreen(
                MDTopAppBar(
                    pos_hint={"top": 1},
                    elevation=4,
                    title="Dashboard",
                    left_action_items=[["menu", lambda x: self.nav_drawer_open()]],
                ),
                #Сторінки
                MDNavigationLayout(
                    MDScreenManager(
                        MDScreen(
                            MDLabel(
                                text="Dashboard",
                                halign="center",
                            ),
                            name="Dashboard",
                        ),
                        MDScreen(
                            MDLabel(
                                text="Power",
                                halign="center",
                            ),
                            name="Power",
                        ),
                        MDScreen(
                            BoxLayout(orientation='vertical',padding=0),  # Групуємо вміст в MDScreen
                            name="Events",
                            on_pre_enter=lambda x: x.add_widget(Table().build())  # Добавляем таблицу при входе на страницу
                        ),
                        id="screen_manager",
                    ),
                    #Панель навігації
                    MDNavigationDrawer(
                        MDScrollView(
                            MDList(
                                OneLineListItem(
                                    text="Dasboard",
                                    on_press=self.switch_screen,
                                ),
                                OneLineListItem(
                                    text="Power",
                                    on_press=self.switch_screen,
                                ),
                                OneLineListItem(
                                    text="Events",
                                    on_press=self.switch_screen,
                                ),
                            ),
                        ),
                        id="nav_drawer",
                        radius=(0, 16, 16, 0),
                    ),
                    id="navigation_layout",
                )
            )
        )
    
    def switch_screen(self, instance_list_item: OneLineListItem):
        self.root.ids.navigation_layout.ids.screen_manager.current = {
            "Dasboard": "Dashboard", "Power": "Power", "Events": "Events"
        }[instance_list_item.text]
        self.root.children[0].ids.nav_drawer.set_state("close")

    def nav_drawer_open(self):
        nav_drawer = self.root.children[0].ids.nav_drawer
        nav_drawer.set_state("open")


