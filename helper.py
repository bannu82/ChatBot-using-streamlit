import textwrap

def to_markdown(text):
  text = text.replace('•', '  *')
  return textwrap.indent(text, '> ', predicate=lambda _: True)
def get_css():
  css =  """
  <style> 
  h1{
    text-align: center; 
  }
  </style>
  
  """
  return css