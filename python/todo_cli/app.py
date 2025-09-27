import sys, json, os
DB = "tasks.json"
tasks = json.load(open(DB)) if os.path.exists(DB) else []
cmd, *args = (sys.argv[1:] or ["help"])
if cmd == "add":
    tasks.append({"t":" ".join(args), "done":False})
elif cmd == "list":
    for i, x in enumerate(tasks, 1):
        status = "✓" if x["done"] else "·"
        print(f"{i}. [{status}] {x['t']}")
elif cmd == "done":
    try:
        i = int(args[0]) - 1
        if 0 <= i < len(tasks):
            tasks[i]["done"] = True
        else:
            print("Invalid task number")
    except (ValueError, IndexError):
        print("Usage: done <number>")
else:
    print("usage: add <task> | list | done <n>")
json.dump(tasks, open(DB,"w"), indent=2)
