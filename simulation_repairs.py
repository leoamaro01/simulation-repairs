def simulate(n: int, s: int, get_explosion_time, get_repair_time) -> float:
    # predefine event names
    explosion = "EXPLOSION"
    repair = "REPAIR"

    # total time transcurred
    time = 0

    # list of upcoming events
    events = []

    # event sort function
    def get_event_time(event: tuple[float, str]) -> float:
        return event[0]

    def sort_events():
        events.sort(key=get_event_time, reverse=True)

    available_backups = s
    on_repair_backlog = 0

    # add the initial explosion events
    for i in range(n):
        events.append((time + get_explosion_time(), explosion))

    sort_events()

    while len(events) > 0:
        e = events.pop()
        time = e[0]

        match e[1]:
            case type if type == explosion:
                print(f"exploded on {time}")
                if available_backups == 0:
                    return time
                
                available_backups -= 1
                events.append((time + get_explosion_time(), explosion))

                if on_repair_backlog == 0:
                    events.append((time + get_repair_time(), repair))
                on_repair_backlog += 1
                
                sort_events()
            case type if type == repair:
                print(f"repaired on {time}")
                available_backups += 1
                on_repair_backlog -= 1

                if on_repair_backlog > 0:
                    print("repairing next machine")
                    events.append((time + get_repair_time(), repair))
                    sort_events()
                else:
                    print("no more machines in backlog")


from random import random

max_repair_time = 10
min_repair_time = 0

min_explosion_time = 5
max_explosion_time = 50

def random_range(min, max):
    return min + random() * (max - min)

print(simulate(10, 10, lambda: random_range(min_explosion_time, max_explosion_time), lambda: random_range(min_repair_time, max_repair_time)))
