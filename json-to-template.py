from json import load

def JsonToTmpl(jsonfile, tmplfile, outputfile):
    with open(jsonfile) as f:
        json_dict = load(f)

    with open(tmplfile) as f:
        template_lines = [line for line in f]

    for i in range(len(template_lines)):
        for keyword in json_dict:
            template_lines[i] = template_lines[i].replace("{{"+keyword+"}}", json_dict[keyword])

    with open(outputfile, "w") as f:
        f.write(''.join(template_lines))

    print(f"{outputfile} done")

JsonToTmpl("english.json", "template.txt", "index.html")
JsonToTmpl("thai.json", "template.txt", "th.html")
