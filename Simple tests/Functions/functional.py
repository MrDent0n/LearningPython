

def main():
    while True:
        result = request_answer(
            "Do you want to continue) [Y/N]:", #question
            "I am sorry u did not understand your answer, please use only y or n"
            #default = False    #default
            # end = n
            #proceed = y
        )
        if result:
            continue
        else:
            break

        print("Signing off")


def request_answer(question, proceed="y", end="n",):
    print("question:", question
          "\n Do you want to quit",
          "\n Yes = y",
          "\n No = N"
          )
    answer = input(question)
    if answer.lower() == end or answer == "":
        return False
    elif answer.lower() == proceed:
        return True
    else:
        print("{}:{}".format(error, answer))
        return default





if __name__ == "__main__":
    main()