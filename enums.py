from enum import Enum


class MuscleGroup(Enum):
    Chest = 1
    Shoulder = 2
    Tricep = 3
    Bicep = 4
    Back = 5
    Legs = 6

class Exercise:
    def __init__(self, name, groups, repetitions=10):
        self.name = name
        self.groups = groups
        self.repetitions = repetitions


class Schedule:
    def __init__(self, name, exercises):
        self.name = name
        self.exercises = exercises

def main():

    # CHEST EXERCISES
    # cce = Chest Compound Exercise
    # cie = Chest Isolation Exercise

    cce1 = Exercise('Incline Bench Press', [MuscleGroup.Tricep, MuscleGroup.Chest, MuscleGroup.Shoulder],15)
    cce2 = Exercise('Barbell Bench Press', [MuscleGroup.Chest, MuscleGroup.Tricep])
    cce3 = Exercise('Dumbbell Bench Press', [MuscleGroup.Chest, MuscleGroup.Tricep])
    cce4 = Exercise('Incline Dumbbell Bench Press', [MuscleGroup.Tricep, MuscleGroup.Chest, MuscleGroup.Shoulder] )
    cie1 = Exercise('Seated Machine Chest Press', [MuscleGroup.Tricep] )
    cie2 = Exercise('Dumbbell Flyes', [MuscleGroup.Chest])
    cie3 = Exercise('Pec-deck Machine', [MuscleGroup.Chest])
    cie4 = Exercise('Cable Crossover', [MuscleGroup.Chest])
    cie5 = Exercise('Low Cable Crossover', [MuscleGroup.Chest])
    cie6 = Exercise('Wide-Grip Dips', [MuscleGroup.Chest, MuscleGroup.Tricep])
    cie7 = Exercise('Dumbell Pullover', [MuscleGroup.Chest])

    # SHOULDER EXERCISES
    #sce = Shoulder Compound Exercises
    #sie = Shoulder Isolation Exercises

    sce1 = Exercise('Military Press', [MuscleGroup.Tricep, MuscleGroup.Shoulder])
    sce2 = Exercise('Seated Dumbbell Shoulder Press', [MuscleGroup.Tricep, MuscleGroup.Shoulder] )
    sce3 = Exercise('Machine Shoulder Press', [MuscleGroup.Tricep, MuscleGroup.Shoulder] )
    sce4 = Exercise('Arnold Press', [MuscleGroup.Tricep, MuscleGroup.Shoulder] )
    sie1 = Exercise('Dumbbell Lateral Raise', [MuscleGroup.Shoulder])
    sie2 = Exercise('One-Arm Cable Lateral Raise', [MuscleGroup.Shoulder])
    sie3 = Exercise('Standing Barbell Shrugs', [MuscleGroup.Shoulder])
    sie4 = Exercise('Rope Face Pull', [MuscleGroup.Shoulder])
    sie5 = Exercise('Bent-Over Lateral Raise', [MuscleGroup.Shoulder])
    sie6 = Exercise('Upright Row', [MuscleGroup.Shoulder])
    sie7 = Exercise('Band Lateral Raise', [MuscleGroup.Shoulder])
    sie8 = Exercise('Front Dumbbell Raise', [MuscleGroup.Shoulder])
    sie9 = Exercise('Band Front Raise', [MuscleGroup.Shoulder])
    sie10 = Exercise('Farmers Walk', [MuscleGroup.Shoulder])
    sie11 = Exercise('Machine Rear-Delt Fly', [MuscleGroup.Shoulder])

    # BACK EXERCISES
    # bce = Back Compound Exercise
    # bie = Back Isolation Exercise

    bce1 = Exercise('Pull Up', [MuscleGroup.Back, MuscleGroup.Bicep])
    bce2 = Exercise('Wide Grip Pulldown', [MuscleGroup.Back, MuscleGroup.Bicep])
    bce3 = Exercise('Chin Up', [MuscleGroup.Back, MuscleGroup.Bicep])
    bce4 = Exercise('Neutral Grip Pull Up', [MuscleGroup.Back, MuscleGroup.Bicep])
    bce5 = Exercise('Deadlift',[MuscleGroup.Back, MuscleGroup.Legs, MuscleGroup.Shoulder])
    bce6 = Exercise('Cable Row', [MuscleGroup.Back, MuscleGroup.Bicep])

    bie1 = Exercise('One-arm Dumbbell Row', [MuscleGroup.Back])
    bie2 = Exercise('Cable Row', [MuscleGroup.Back])
    bie3 = Exercise('Cable Reverse Butterfly', [MuscleGroup.Back])
    bie4 = Exercise('Back Extension', [MuscleGroup.Back])
    bie5 = Exercise('Inverted Row', [MuscleGroup.Back])
    bie6 = Exercise('Barbell Row', [MuscleGroup.Back])
    bie7 = Exercise('T-bar Row', [MuscleGroup.Back])
    bie8 = Exercise('One-Arm Lat Machine Pulldowns Neutral Grip', [MuscleGroup.Back])
    bie9 = Exercise('Cable Pulldowns', [MuscleGroup.Back])

    # LEG EXERCISES
    # lce = Leg Compound Exercises
    # lie = Leg Isolation Exercises

    lce1 = Exercise('Squat', [MuscleGroup.Legs])
    lce2 = Exercise('Leg Press', [MuscleGroup.Legs])
    lce3 = Exercise('Walking Lounge', [MuscleGroup.Legs])
    lce4 = Exercise('Bulgarian Split Squat', [MuscleGroup.Legs])
    lce5 = Exercise('Barbell Hip Thrust', [MuscleGroup.Legs])
    lce6 = Exercise('Jump Squat', [MuscleGroup.Legs])

    lie1 = Exercise('Romanian Deadlift', [MuscleGroup.Legs])
    lie2 = Exercise('Single Leg Curl', [MuscleGroup.Legs])
    lie3 = Exercise('Leg Extension', [MuscleGroup.Legs])
    lie4 = Exercise('Bodyweight Calf Raise', [MuscleGroup.Legs])
    lie5 = Exercise('Seated Calf Raise', [MuscleGroup.Legs])

    # BICEP EXERCISES
    # be = Bicep Exercise

    be1 = Exercise('Incline Inner-Biceps Curl', [MuscleGroup.Bicep])
    be2 = Exercise('EZ-Bar Curl', [MuscleGroup.Bicep])
    be3 = Exercise('Regular-Grip Barbell Curl', [MuscleGroup.Bicep])
    be4 = Exercise('Standing Dumbbell Bicep Cur', [MuscleGroup.Bicep])
    be5 = Exercise('Rope Cable Hammer Curls', [MuscleGroup.Bicep])
    be6 = Exercise('Dumbbell Preacher Curl', [MuscleGroup.Bicep])

    # TRICEP EXERCISES
    # te = Tricep Exercise

    te = Exercise('Lying Triceps Extension', [MuscleGroup.Tricep])
    te = Exercise('Tricep Dips', [MuscleGroup.Tricep])
    te = Exercise('Close Grip Bench Press', [MuscleGroup.Tricep])
    te = Exercise('Rope Tricep Pushdown', [MuscleGroup.Tricep])
    te = Exercise('Overhead Triceps Extension', [MuscleGroup.Tricep])


    # USER INPUT

    weekdays = int(input("How many days per week do you want to work out? (1-6): "))

    if weekdays == 1:
        print("hejhej")


    ce = Schedule('sdfs', [e1, e2])
    for ex in e.groups:
        if ex == MuscleGroup.Chest:


if __name__ == '__main__':
    main()
