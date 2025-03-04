def deep_recursive_find_map(target:any,structure:any) -> list:
    if target == structure:
        return []
        
    if isinstance(structure,list):
    
        for i,s in enumerate(structure):
            if target == s:
                return [i]
            if isinstance(s,(dict,list)):
                result = deep_recursive_find_map(target,s)
                if result:
                    return [i,*result]

    if isinstance(structure,dict):
            for k,v in structure.items():
                if v == target : 
                   return [k]
                if isinstance(v,(dict,list)):
                    result = deep_recursive_find_map(target,v)
                    if result:
                        return [k,*result]
                       
    return None