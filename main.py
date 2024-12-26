from customtkinter import CTkLabel

from components import AppLayout, Button, Console, URLInputBox
from constant import GLOBAL_PADDING_Y, GLOBAL_PADDING_X
from utils import onclick_download, onclick_clear

layout = AppLayout(title="YouTube Audio Downloader")
layout.set_column_config(0, 1)
app = layout.app

title = CTkLabel(app, text="YouTube Audio Downloader", fg_color="transparent")
title.grid(row=0, column=0, pady=(GLOBAL_PADDING_Y, 0))

url_input_box = URLInputBox(app, label_row=1, label_padding_x=GLOBAL_PADDING_X, textbox_padding_x=GLOBAL_PADDING_X)

clear_button = Button(app, text="Clear", row=3, column=0,
                      padding_x=GLOBAL_PADDING_X, padding_y=(10, 0), sticky="w",
                      command=lambda: onclick_clear(url_input_box))

console = Console(app, label_row=4, label_padding_x=GLOBAL_PADDING_X, textbox_padding_x=GLOBAL_PADDING_X)

download_button = Button(app, text="Download", row=6, column=0,
                         padding_x=GLOBAL_PADDING_X, padding_y=GLOBAL_PADDING_Y, button_color="green",
                         command=lambda: onclick_download(url_input_box,
                                                          console,
                                                          download_button,
                                                          clear_button))

layout.start()
