from pyautogui import click, moveTo

icon_volume_x = 1794
icon_volume_y = 1055

disp_rep_x = 1769
disp_rep_y = 957

mouse_descanso_x = 528
mouse_descanso_y = 335

click(icon_volume_x, icon_volume_y, button='right')
click(disp_rep_x, disp_rep_y)
moveTo(mouse_descanso_x, mouse_descanso_y)
