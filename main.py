def deep_recursive_find(target:any,structure:any) -> list:
    if target == structure:
        return []
    if (isinstance(target,(str,list))) and isinstance(structure,str):
        return None
    
    for i,s in enumerate(structure):
        if target == s:
            return [i,target]
        
        if isinstance(s,dict):
            for k,v in s.items():
                if v == target : 
                   return [i,k,target]
                if isinstance(v,dict):
                   result_dict = deep_recursive_find(target,v);
                   if result_dict:
                       return [i,k,target]
                   
        if isinstance(s,list):
            result = deep_recursive_find(target,s)
            if result:
                return [i,target]
    return None

print(deep_recursive_find("Hello World",["Hello","World",{ 'value': [ "Hello World"] }, ["Hello World"]]))
