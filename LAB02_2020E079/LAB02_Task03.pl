% Facts and Rules
man(marcus).
pompeian(marcus).
ruler(caesar).

pompeian(X) :- roman(X).
roman(X) :- loyalto(X, caesar).
roman(X) :- hate(X, caesar).

loyalto(X, skolem_constant).

person(X) :- ruler(Y), tryassassinate(X, Y), not(loyalto(X, Y)).
tryassassinate(marcus, caesar).

man(X) :- person(X).

% Query to prove: Marcus hates Caesar
prove_hate :-
    hate(marcus, caesar),
    write('Marcus hates Caesar').

% Run the program
:- prove_hate.
