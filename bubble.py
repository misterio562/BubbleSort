import flet as ft
import random
import time

def main(page: ft.Page):

    def create_containers(number):
        container_list = []

        for _ in range(number):
            container_list.append(
                ft.Container(
                    content= ft.Text(value=random.randint(1,100)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.AMBER_200,
                    border_radius=25
                )
            )
        return container_list

    row = ft.Row(
        controls=(create_containers(10))
    )

    page.add(row)


    array = row.controls
    time.sleep(5)

    n = len(array)
    for i in range(n):
        for j in range (0, n-i-1):
            array[j].bgcolor = ft.colors.ORANGE
            array[j+1].bgcolor = ft.colors.ORANGE
            time.sleep(2)
            page.update()
            if array[j].content.value > array[j+1].content.value:
                array[j] , array[j+1] = array[j+1], array[j]
            array[j].bgcolor = ft.colors.YELLOW
            array[j+1].bgcolor = ft.colors.YELLOW
        array[n-i-1].bgcolor = ft.colors.GREEN
    page.update()

ft.app(target=main)