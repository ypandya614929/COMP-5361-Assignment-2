# COMP-5361-Assignment-2
COMP-5361-Assignment-2

## To setup virtualenv if not already
    
    virtualenv -p python3.6 env
    source env/bin/activate

## Available Operators

    NEGATION OPERATORS = ¬, ~, !
    CONJUNCTION OPERATORS = ∧, ^, &
    DISJUNCTION OPERATORS = ∨, v, |, V
    EX-OR OPERATORS = ⊕
    CONDITIONAL OPERATORS = =>, ->, →
    BI-CONDITIONAL OPERATORS = ↔
    DOUBLE_NEGATION_OPERATORS = "~~", "!!", "¬¬"

## Available Operand (Variable) Values:

    NEGATIVE VALUES = F, f, False, false, 0
    POSITIVE VALUES = T, t, True, true, 1


## Run Program
#### python asgn2.py
    
    - When the rogram runs user is displayed with following menu in the console
    
        COMP-5361 Assignment-2 Menu
        -------------------------------------------------------
        1. Produce output from truth assignments
        2. Display truth table and propositional equivalences
        3. Exit
        
        Select:
        
    - The user need to select any one of the available option at a time, otherwise 
    it will raise an error for invalid choice.
     
    - After selecting either of the choice 1 or 2, user need to give an input of propositional 
    logic equation. If the equation is invalid user need to repeat the same process again.
      
        Please enter valid propositional logic equation : ((A ∧ B) => C)
      
    - For choice 1, user need to give boolean inputs for variables in order to compute output 
    from the truth assignments.

        Please enter bool value for A : True
        Please enter bool value for B : True
        Please enter bool value for C : False

    - Then, for choice 1 below result will be displayed.

        ===============================================================================================
        The value of expression ( ( A ∧ B ) => C ) : False
        ===============================================================================================
        
    - And, for choice 2 below result will be displayed.
        
        ====    ====    ====    ==========      =================
        A       B       C       (A ∧ B)         ((A ∧ B) => C)   
        ====    ====    ====    ==========      =================
        False   False   False   False           True             
        False   False   True    False           True             
        False   True    False   False           True             
        False   True    True    False           True             
        True    False   False   False           True             
        True    False   True    False           True             
        True    True    False   True            False            
        True    True    True    True            True             
        =======================================================
        Solution :  Contingency
        =======================================================



# Test cases
## Question 1

    COMP-5361 Assignment-2 Menu
    -------------------------------------------------------
    1. Produce output from truth assignments
    2. Display truth table and propositional equivalences
    3. Exit

    Select: 1

    Please enter valid propositional logic equation : ((P1 ∧ P2) ∨ (P3 ∧ True)) ∨ ((¬P1 ∧ ¬P3) ∧ P2)

    Please enter bool value for P1 : True
    Please enter bool value for P2 : False
    Please enter bool value for P3 : True

    ===============================================================================================
    The value of expression ( ( P1 ∧ P2 ) ∨ ( P3 ∧ True ) ) ∨ ( ( ¬ P1 ∧ ¬ P3 ) ∧ P2 ) : True
    ===============================================================================================
    
  
  ## Question 2
  #### Question 2(a)
  
    COMP-5361 Assignment-2 Menu
    -------------------------------------------------------
    1. Produce output from truth assignments
    2. Display truth table and propositional equivalences
    3. Exit

    Select: 2

    Please enter valid propositional logic equation : (¬P1 ∧ (P1 ∨ P2)) → P2

    =====   =====   ======  ============    ====================    ===========================
    P1      P2      ¬P1     (P1 ∨ P2)       (¬P1 ∧ (P1 ∨ P2))       ((¬P1 ∧ (P1 ∨ P2)) → P2)   
    =====   =====   ======  ============    ====================    ===========================
    False   False   True    False           False                   True                       
    False   True    True    True            True                    True                       
    True    False   False   True            False                   True                       
    True    True    False   True            False                   True                       
    =======================================================
    Solution :  Tautology
    =======================================================


#### Question 2(b)

    COMP-5361 Assignment-2 Menu
    -------------------------------------------------------
    1. Produce output from truth assignments
    2. Display truth table and propositional equivalences
    3. Exit

    Select: 2

    Please enter valid propositional logic equation : P2 ∧ (P1 → ¬P2) ∧ (¬P1 → ¬P2)

    =====   =====   ======  =============   ====================    ======  ==============  ====================================
    P1      P2      ¬P2     (P1 → ¬P2)      (P2 ∧ (P1 → ¬P2))       ¬P1     (¬P1 → ¬P2)     ((P2 ∧ (P1 → ¬P2)) ∧ (¬P1 → ¬P2))   
    =====   =====   ======  =============   ====================    ======  ==============  ====================================
    False   False   True    True            False                   True    True            False                               
    False   True    False   True            True                    True    False           False                               
    True    False   True    True            False                   False   True            False                               
    True    True    False   False           False                   False   True            False                               
    =======================================================
    Solution :  Contradiction
    =======================================================



#### Question 2(c)
    
    COMP-5361 Assignment-2 Menu
    -------------------------------------------------------
    1. Produce output from truth assignments
    2. Display truth table and propositional equivalences
    3. Exit

    Select: 2

    Please enter valid propositional logic equation : (P1 → (P2 → P3)) → ((P1 → P2) → P3)

    =====   =====   =====   ============    ===================     ============    ===================     ========================================
    P1      P2      P3      (P2 → P3)       (P1 → (P2 → P3))        (P1 → P2)       ((P1 → P2) → P3)        ((P1 → (P2 → P3)) → ((P1 → P2) → P3))   
    =====   =====   =====   ============    ===================     ============    ===================     ========================================
    False   False   False   True            True                    True            False                   False                                   
    False   False   True    True            True                    True            True                    True                                    
    False   True    False   False           True                    True            False                   False                                   
    False   True    True    True            True                    True            True                    True                                    
    True    False   False   True            True                    False           True                    True                                    
    True    False   True    True            True                    False           True                    True                                    
    True    True    False   False           False                   True            False                   True                                    
    True    True    True    True            True                    True            True                    True                                    
    =======================================================
    Solution :  Contingency
    =======================================================

