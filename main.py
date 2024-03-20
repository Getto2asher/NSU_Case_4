import locals as l

day_num = int(input(f"{l.day_of_the_day} ({l.MON}, {l.TUE}, ..., {l.SUN}): "))


def even_day(day_num):
    return day_num % 2 == 0


match day_num:
    case 1 | 2 | 3 | 4 | 5:
        print(l.weekday)
        if even_day(day_num) == True:
            print(l.even_day)
        else:
            print(l.not_even_day)
            pairs = int(input((l.lessons)))
            print(l.mood_var)
            mood = int(input(l.mood))
            result = print(pairs // 2) if mood == 3 else print(l.light_day)
            if mood == 1:
                print(l.mood_variant_1)
            if mood == 2:
                print(l.mood_variant_2)


    case 6 | 7:
        print(l.weekend)
