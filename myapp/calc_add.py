import flet as ft
from random import randint

#clickするたびに問題をかえたい

def create_equistion():
    one = randint(1, 10)
    two = randint(1,10)
    right_answer = one + two
    return (f"{one} + {two} = ", right_answer)


def main(page: ft.Page):
    print("start")
    equision, right_answer = create_equistion()
    your_answer_ref = ft.Ref[ft.TextField]()
    question_sentence_ref = ft.Ref[ft.TextField]()
    question_sentence = ft.Text(ref=question_sentence_ref, value=equision)
    your_answer_field = ft.TextField(ref=your_answer_ref, label="答え", autofocus=True)
    
    #答えボタンをクリック
    def answered(e):
        print("click")
        try:
            yours = int(your_answer_ref.current.value)
                
            color = "blue"
            mark = "○"
            if right_answer != yours:
                color = "red"
                mark = "×"
            
            page.add(
                ft.Row(controls=[
                    ft.Text(equision + f"{yours}"),
                    ft.Text(value=mark, color=color)
                ]
                )
            )
            your_answer_ref.current.value = ""
            your_answer_ref.current.focus()
        #数字でないものが打ち込まれた場合
        except:
            your_answer_field.error_text = "数値を入れてください"
        equision, right_answer = create_equistion()
        question_sentence_ref.current.value = equision
        print(equision)
        page.update()
        
        print("click finished")
    #答えボタンクリック関数終了
    
    question = ft.Row(controls=[
        question_sentence,
        your_answer_field,
        ft.ElevatedButton(text="答え", on_click=answered)
    ])
    page.add(
        question
    )
    
    
ft.app(target=main)