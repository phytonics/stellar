import commonmark
import sys

with open(f'{sys.argv[1]}.md', 'r') as myfile:
  text = myfile.read()

parser = commonmark.Parser()
ast = parser.parse(text)

# Returns the text from markdown, stripped of the markdown syntax itself
def ast2text(astNode):
    walker = astNode.walker()
    acc = "";
    iterator = iter(walker)
    while True:
        try:
            (current, entering) = next(iterator)
        except StopIteration:
            break  # Iterator exhausted: stop the loop
        else:
            print("- - - - - - -")
            print(f"{entering} \"{current.t}\": \"{current.literal}\"")
            # Add the text
            if current.literal:
                acc += current.literal
            # Add in the missing line breaks
            if current.t == "linebreak":
                acc += "\n"
            if current.t == "paragraph" and entering == False:
                acc += "\n\n"
            if current.t == "heading" and entering == False:
                acc += "\n"
    print("")
    return acc.strip()


print(ast2text(ast))