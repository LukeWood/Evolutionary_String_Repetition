y = [17;16;14;13;10;9;9;8;8;7;6;5;5;3;3;3;1;1;1;1;1;];ymax=max(y);
y=ymax-y;
y=y/ymax;
y = y*100;plot(y,'b-o');
xlabel('Generations');
ylabel('Accuracy (%)');
title('Evolutionary String Repetition');