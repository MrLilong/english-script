global string, last_node, current_value, nodes, depth,rollback_depths,OK
global verbose,use_wordnet,in_pipe,result,in_args
global tokenstream,current_token,current_type,current_word,current_line

_verbose =  True # False angel.verbose() and not angel.raking()  # false
very_verbose = _verbose

use_tree=False
use_wordnet=False
in_pipe=False
OK="OK"
interpret=False

interpret = True
did_interpret = True
javascript = ''
context = ''
variables = {}
variableTypes = {}
variableValues = {}  # ={nill: None)
svg = []

string=""
tokenstream=[] # tuple:
token_number=0
current_type=0
current_word=''
current_line=''
current_token=None

lines = []
original_string = ""  # for string_pointer ONLY!!
string = ""
line_number = 0
last_pattern = None

# bash_methods=["say"]
c_methods = ['printf']
builtin_methods = ['puts', 'print']  # "puts"=>x_puts !!!
core_methods = ['show', 'now', 'yesterday', 'help']  # _try(difference)
methods = {}  # name->method-node
OK = 'OK'
result = ''
listeners = []
nodes = []

rollback = []
tree = []
interpret_border = -1
no_rollback_depth = -1
rollback_depths = []
max_depth = 160  # world this method here to resolve the string
negated=False
in_params=0
depth=0
current_node=None
current_value=None
parser=globals()
context=None
throwing=False
result=None
def is_number(s):            #isint isnum
  return isinstance(s,int) or isinstance(s,float) or isinstance(s,str) and s.isdigit() # is number isnumeric

