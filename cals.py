import functools

def solution (cals, d:int, min:int, max:int):
    day_count = 0
    total = 0
    points = 0
    for cal in cals:
        total += cal
        day_count += 1
        if day_count == d:
            if total < min:
                points -= 1
            elif total > max:
                points += 1
            day_count = 0
            total =0
    return points



if __name__ == '__main__':
    cals = [100, 200, 350, 400]
    days = 2
    print(solution(cals=cals, d=days, min=250, max=300))