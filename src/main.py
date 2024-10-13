from CompiScript.compiscriptLexer import compiscriptLexer
from CompiScript.compiscriptParser import compiscriptParser
from Utils.CustomException import ThrowingErrorListener
from ParseTree.parse_tree import TreeVisualizer
from antlr4 import FileStream, CommonTokenStream
from SemanticAnalyzer.semantic_analyzer import SemanticAnalyzer

def main():
    
    # Get the input file and create a file stream
    input_file = 'src/Examples/test.cspt'
    input_stream = FileStream(input_file)

    # Create the lexer and use a custom error listener
    lexer = compiscriptLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())

    # Create the token stream
    token_stream = CommonTokenStream(lexer)

    # Create the parser and use a custom error listener
    parser = compiscriptParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())

    # Parse the input and get the parse tree
    parse_tree = parser.program()

    # Create a TreeVisualizer object and visit the parse tree
    tree_visualizer = TreeVisualizer(input_file)
    tree_visualizer.visit(parse_tree)
    tree_visualizer.render(output_file=tree_visualizer.name, 
                           format='png', 
                           output_dir='src/ParseTree/Output')
    
    # Create a SemanticAnalyzer object and visit the parse tree
    semantic_analyzer = SemanticAnalyzer()
    semantic_analyzer.visit(parse_tree)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)