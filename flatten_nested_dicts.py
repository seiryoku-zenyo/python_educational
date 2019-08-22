# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:57:09 2019

@author: Vasco
"""

def flatten(dictio):
    new_key=[]
    fin_ans = {}  
    
    def into_dict(x):
        for i in x.keys():
            new_key.append(i)
            val = x.get(i)
            if isinstance(val,dict):
                if len(val) < 1:
                        ans={'/'.join(new_key):''}
                        print(ans)
                        fin_ans.update(ans)
                        new_key.remove(new_key[-1]) 
                        
                else:
                    into_dict(val) #recursivity
                    new_key.remove(new_key[-1])
                  
            else:
                ans={'/'.join(new_key):val}
                print(ans)
                fin_ans.update(ans)
                new_key.remove(new_key[-1])
                                     
    into_dict(dictio)
    print('\n',fin_ans, ' success!\n')
    return fin_ans

if __name__ == '__main__':
# =============================================================================
#     test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
#     print(' Input: {}'.format(test_input))
#     print('Output: {}'.format(flatten(test_input)))
# =============================================================================

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
         {"key": {"deeper": {"more": {"enough": "value"}}}}
     ) == {'key/deeper/more/enough': 'value'}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"

    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}, 'Last One'
    print('You all set. Click "Check" now!')

