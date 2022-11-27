import json

filename = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as f:
        dict = []
        for i, line in enumerate(f):
            fields = line.strip(new_line).split(delimiter)
            if i == 0:
                heads = fields
                continue

            dict.append({})

            for i, _ in enumerate(heads):

                dict[-1][heads[i]] = fields[i]
    return dict

print(json.dumps(csv_to_list_dict(filename), indent=4))