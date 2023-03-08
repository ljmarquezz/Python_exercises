def solution (animals:str, f):
    animals_list = list(map(lambda x:x.lower(), animals.split()))
    animals_wo_forbidden = list(filter(lambda x:not x in f, animals_list))
    most_repeated_animal = ""
    times_repeated = 0
    for animal in animals_wo_forbidden:
        times = animals_wo_forbidden.count(animal)
        if times > times_repeated:
            times_repeated = times
            most_repeated_animal = animal
    return most_repeated_animal


if __name__ == '__main__':
    animals = 'monkey biRd Dog Cat CAT MonKey bIrd cat dOg elephant BIRD mOnKeY birD'
    forbidden = ('monkey', 'bird')
    print(solution(animals=animals, f=forbidden))