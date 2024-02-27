class Computer:
    def __init__(self) -> None:
        self.times_broken = 0

    def break_machine(self):
        self.times_broken += 1


def simulate(n: int, s: int, get_explosion_time, get_repair_time, max_time = 0) -> float:
    # predefine event names
    explosion = "EXPLOSION"
    repair = "REPAIR"

    # total time transcurred
    time = 0

    # list of upcoming events
    events = []

    # event sort function
    def get_event_time(event: tuple[float, str, Computer]) -> float:
        return event[0]

    def sort_events():
        events.sort(key=get_event_time, reverse=True)

    available_backups = []
    on_repair_backlog = []

    # add backup computers
    for i in range(s):
        c = Computer()
        available_backups.append(c)

    # add the initial computers
    for i in range(n):
        c = Computer()
        events.append((time + get_explosion_time(0), explosion, c))

    sort_events()

    while len(events) > 0:
        e = events.pop()
        time = e[0]

        if max_time > 0 and time > max_time:
            return time

        match e[1]:
            case type if type == explosion:
                # print(f"exploded on {time}")
                if len(available_backups) == 0:
                    return time
                
                e[2].break_machine()

                backup = available_backups.pop()
                events.append((time + get_explosion_time(backup.times_broken), explosion, backup))

                if len(on_repair_backlog) == 0:
                    events.append((time + get_repair_time(), repair, e[2]))
                on_repair_backlog.append(e[2])
                sort_events()
            case type if type == repair:
                # print(f"repaired on {time}")
                available_backups.append(e[2])
                on_repair_backlog.remove(e[2])

                if len(on_repair_backlog) > 0:
                    # print("repairing next machine")
                    events.append((time + get_repair_time(), repair, on_repair_backlog[0]))
                    sort_events()
                # else:
                #     print("no more machines in backlog")