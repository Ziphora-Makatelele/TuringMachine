Class TuringMachine:
    def_init_(self, tape, blank_symbol, initial_state, transition_function)
        self.tape = (tape)
        self.blank_symbol = blank_symbol
        self.head_position = 0
        self.current_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function
        
    def step(self):
        current_symbol = self.tape[slef.head_position]
            if(self.current_state, current_symbol) in self.transition_function
        next_state, write_symbol, move_direction = self.transition[(self.current_state, current_symbol)]
        self.tape[self.head_position] = write_symbol
        self.current_state = next_state
        
            if move_direction == 'R':
        self.head_position += 1
        self.head_position >= len(self.tape)
        self.tape.append(self.blank_symbol)
        
            elif move_direction == 'L':
        self.head_position -= 1
        
            if self.head_position < 0:
        self.tape.insert(0, self.blank_symbol)
        self.head_position = 0
        
        else:
            self.current_state = None
        
    def run(self):
        while self.current_state not i self.final_states and self.current_state is not None:
            self.step() return.join (self.tape).strip(self.blank_symbol)
            
    tape = "1101"
    blank_symbol = " "
    initial_state = "q0"
    final_states = {qf}
    
    #Transition fuction: 
        (state, symbol) -> (next_state, write_symbol, move_direction)
        
        transition_function: {
        ("q0","1") : ("q0","1","R")
        ("q0","0") : ("q0"," ","N")
        #stop when blank is encountered
        }
        
    tm = TuringMachine(tape, blank_symbol, initial_state, final_states, transition_function)
    result = tm.run()
    print("Final tape content: " , result)