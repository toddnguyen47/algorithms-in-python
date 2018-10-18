import re

template_file_name = "aoe2_wiki_template.txt"

def find_input():
    '''
    Sample input: {{2icons|Inquisition}}
    '''
    input2 = input("Enter in units: ")
    pattern = r"(?:[\s\S]*?\|)([\s\S]*[^}}])"
    matchObj = re.match(pattern, input2)
    if matchObj:
        find_in_template(matchObj.group(1))
    else:
        print("No match")
        

def find_in_template(str_pattern):
    pattern = "".join(("(?:\{\{\{1\}\}\}\|", str_pattern, "\|)"))
    pattern = "".join((pattern, "(\[\[[\s\S]*?)(?:\<\/span\>)"))
    
    with open(template_file_name, "r") as file:
        template = file.read()

    matchObj = re.search(pattern, template)
    if matchObj:
        smaller_str = matchObj.group(1)
        new_pattern = r"\[\[[\s\S]*?\]\]"
        new_match_obj = re.findall(new_pattern, smaller_str)
        if new_match_obj:
            image = new_match_obj[0]
            image = re.sub("{{{[\S]*?}}}", "22", image)
            unit_name = new_match_obj[1]
            
            with open("output.txt", "w") as file:
                temp_str = "".join((image, " ", unit_name))
                file.write(temp_str)
                print(temp_str)
                
        
    else:
        print("No match")



if __name__ == "__main__":
    find_input()
