% Even with fairest rule, the redistribution prcess will induce large gap between the wealthy and poor.

numofpeople = 100; generations = 20000; totalproperty = 100; 
numofeffort = 0; % The number of people who pay more efforts than others

directions = [1:numofpeople,1:numofeffort];
peoples = totalproperty*ones(1,numofpeople);

for generation = 1:generations
    choice = randi(numofpeople+numofeffort,1,numofpeople);
    for i = 1:numofpeople
        if peoples(i) > 0
            peoples(directions(choice(i))) = peoples(directions(choice(i))) + 1;
            peoples(i) = peoples(i) - 1;
        end
    end
end

figure(1);
title('Property and players');
bar(peoples); xlim([1,100]);

figure(2);
title('Rich and poverty');
bar(sort(peoples)); xlim([1,100]);

figure(3);
title('Redistribution of property');
hist(peoples); 