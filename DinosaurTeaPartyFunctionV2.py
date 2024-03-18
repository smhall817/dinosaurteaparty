def play():

    import random
    
    dinosaurs = [
        {'name':'Amelia','green':True,'orange':False,'purple':False,'hat':True,
         'pet':False,'spines':True,'teeth':False,'glasses':False,'tea':True,
         'tail':False,'stripes':False,'flower':True,'cake':False,'jewelry':True,
         'dots':False
         },
        {'name':'Yorick','green':True,'orange':False,'purple':False,'hat':False,
          'pet':False,'spines':False,'teeth':True,'glasses':False,'tea':True,
          'tail':False,'stripes':False,'flower':True,'cake':False,'jewelry':False,
          'dots':False
         },
        {'name':'Eleanor','green':True,'orange':False,'purple':False,'hat':True,
          'pet':False,'spines':False,'teeth':False,'glasses':False,'tea':True,
          'tail':False,'stripes':False,'flower':True,'cake':True,'jewelry':True,
          'dots':False
         },
        {'name':'Lloyd','green':True,'orange':False,'purple':False,'hat':False,
          'pet':False,'spines':False,'teeth':True,'glasses':False,'tea':True,
          'tail':True,'stripes':True,'flower':False,'cake':True,'jewelry':False,
          'dots':False
         },
        {'name':'Tabitha','green':True,'orange':False,'purple':False,'hat':True,
          'pet':False,'spines':False,'teeth':True,'glasses':True,'tea':True,
          'tail':False,'stripes':False,'flower':True,'cake':False,'jewelry':True,
          'dots':False
         },
        {'name':'Ulysses','green':True,'orange':False,'purple':False,'hat':True,
          'pet':False,'spines':False,'teeth':False,'glasses':True,'tea':False,
          'tail':False,'stripes':False,'flower':False,'cake':False,'jewelry':False,
          'dots':True
         },
        {'name':'Gerald','green':True,'orange':False,'purple':False,'hat':True,
          'pet':False,'spines':False,'teeth':True,'glasses':False,'tea':False,
          'tail':False,'stripes':False,'flower':False,'cake':True,'jewelry':False,
          'dots':False
         },
        {'name':'Nigel','green':True,'orange':False,'purple':False,'hat':True,
          'pet':False,'spines':True,'teeth':True,'glasses':False,'tea':False,
          'tail':True,'stripes':True,'flower':False,'cake':True,'jewelry':False,
          'dots':False
         },
        {'name':'Vincent','green':False,'orange':True,'purple':False,'hat':True,
          'pet':False,'spines':False,'teeth':True,'glasses':True,'tea':True,
          'tail':False,'stripes':False,'flower':False,'cake':False,'jewelry':False,
          'dots':True
         },
        {'name':'Winston','green':False,'orange':True,'purple':False,'hat':True,
          'pet':False,'spines':True,'teeth':False,'glasses':False,'tea':False,
          'tail':True,'stripes':False,'flower':True,'cake':False,'jewelry':True,
          'dots':True
         },
        {'name':'Quinton','green':False,'orange':True,'purple':False,'hat':False,
          'pet':True,'spines':False,'teeth':False,'glasses':True,'tea':False,
          'tail':False,'stripes':True,'flower':False,'cake':True,'jewelry':True,
          'dots':False
         },
        {'name':'Xavier','green':False,'orange':True,'purple':False,'hat':True,
          'pet':False,'spines':True,'teeth':True,'glasses':False,'tea':True,
          'tail':True,'stripes':True,'flower':False,'cake':False,'jewelry':False,
          'dots':False
         },
        {'name':'Reginald','green':False,'orange':True,'purple':False,'hat':False,
          'pet':False,'spines':True,'teeth':False,'glasses':True,'tea':False,
          'tail':True,'stripes':True,'flower':False,'cake':True,'jewelry':False,
          'dots':False
         },
        {'name':'Sebastian','green':False,'orange':True,'purple':False,'hat':True,
          'pet':True,'spines':True,'teeth':True,'glasses':False,'tea':False,
          'tail':True,'stripes':False,'flower':False,'cake':True,'jewelry':False,
          'dots':False
         },
        {'name':'Kenneth','green':False,'orange':False,'purple':True,'hat':False,
          'pet':False,'spines':False,'teeth':False,'glasses':False,'tea':False,
          'tail':False,'stripes':False,'flower':True,'cake':True,'jewelry':False,
          'dots':False
         },
        {'name':'Dennis','green':False,'orange':False,'purple':True,'hat':True,
          'pet':False,'spines':False,'teeth':True,'glasses':True,'tea':True,
          'tail':False,'stripes':False,'flower':True,'cake':False,'jewelry':False,
          'dots':False
         },
        {'name':'Beatrice','green':False,'orange':False,'purple':True,'hat':True,
          'pet':True,'spines':False,'teeth':False,'glasses':True,'tea':True,
          'tail':False,'stripes':False,'flower':True,'cake':False,'jewelry':False,
          'dots':False
         },
        {'name':'Carlton','green':False,'orange':False,'purple':True,'hat':False,
          'pet':True,'spines':True,'teeth':True,'glasses':False,'tea':True,
          'tail':False,'stripes':True,'flower':False,'cake':False,'jewelry':False,
          'dots':False
         },
        {'name':'Harriet','green':False,'orange':False,'purple':True,'hat':False,
          'pet':False,'spines':True,'teeth':False,'glasses':False,'tea':True,
          'tail':False,'stripes':False,'flower':False,'cake':True,'jewelry':True,
          'dots':True
         },
        {'name':'Jeannine','green':False,'orange':False,'purple':True,'hat':True,
          'pet':True,'spines':False,'teeth':False,'glasses':True,'tea':False,
          'tail':False,'stripes':False,'flower':False,'cake':True,'jewelry':True,
          'dots':False
         }
        ]
    
    questions = ['green','orange','purple','hat','pet','spines','teeth','glasses',
                 'tea','tail','stripes','flower','cake','jewelry','dots']
    
    answer = random.choice(dinosaurs)
    q_num = 1
    
    
    while len(dinosaurs) > 0:
        
        ### If only one dinosaur remains, break loop
        if len(dinosaurs) == 1:
            break
        
        else:
            ### If two colors have been asked and both were wrong, remove remaining color from question list
            if 'green' in questions and 'purple' not in questions and 'orange' not in questions:
                questions.remove('green')
            if 'orange' in questions and 'purple' not in questions and 'green' not in questions:
                questions.remove('orange')
            if 'purple' in questions and 'orange' not in questions and 'green' not in questions:
                questions.remove('purple')
            
            ### Remove questions for which all remaining dinosaurs have the same answer
            for question in reversed(questions):
                s = set([d.get(question) for d in dinosaurs])
                if len(s) == 1:
                    questions.remove(question)                
      
    
            ### Choose a question to ask
            random.shuffle(questions)
            quantities = []
            for question in questions:
                i = 0
                for d in dinosaurs:
                    if d.get(question) == True:
                        i += 1
                quantities.append(i)
            idx = min(range(len(quantities)), key=lambda i: abs(quantities[i]-(len(dinosaurs)/2)))
            q = questions[idx]
    
    
            ### Remove any dinosaurs for which the answer does not match
            for d in reversed(dinosaurs):
                if d.get(q) != answer.get(q):
                    dinosaurs.remove(d)
                    
            ### If color is guessed, remove other colors from question list
            if q == 'green' and answer.get('green') == True:
                for d in reversed(dinosaurs):
                    if d.get('orange') == True or d.get('purple') == True:
                        dinosaurs.remove(d)
                if 'orange' in questions:
                    questions.remove('orange')
                if 'purple' in questions:
                    questions.remove('purple')
            elif q == 'orange' and answer.get('orange') == True:
                for d in reversed(dinosaurs):
                    if d.get('green') == True or d.get('purple') == True:
                        dinosaurs.remove(d)
                if 'orange' in questions:
                    questions.remove('orange')
                if 'purple' in questions:
                    questions.remove('purple')
            elif q == 'purple' and answer.get('purple') == True:
                for d in reversed(dinosaurs):
                    if d.get('green') == True or d.get('orange') == True:
                        dinosaurs.remove(d)
                if 'green' in questions:
                    questions.remove('green')
                if 'orange' in questions:
                    questions.remove('orange')   
    
            ### Remove asked question from question list
            if q in questions:
                questions.remove(q)
            ### Increment question counter
        q_num += 1
    
    
    return([q_num - 1, answer.get('name')])
play()