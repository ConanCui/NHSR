x = 0:0.01:10;
y1 = sigmoid(x);
y2 = tanh(x);
y3 = (1 - y1).*y1;
y4 =  1 - y2.^2;
figure(1)
plot(x,y1,'--b',...
       'LineWidth',2,...
       'MarkerSize',5,...
       'MarkerEdgeColor','b',...
       'MarkerFaceColor',[0.5,0.5,0.5])
hold on
plot(x,y2,'--r',...
      'LineWidth',2,...
       'MarkerSize',5,...
       'MarkerEdgeColor','r',...
       'MarkerFaceColor',[0.5,0.5,0.5])
hold on 
plot(x,y3,'b',...
      'LineWidth',2,...
       'MarkerSize',5,...
       'MarkerEdgeColor','r',...
       'MarkerFaceColor',[0.5,0.5,0.5])
hold on 
plot(x,y4,'r',...
      'LineWidth',2,...
       'MarkerSize',5,...
       'MarkerEdgeColor','r',...
       'MarkerFaceColor',[0.5,0.5,0.5])

   
legend('sigmoid','tanh','dsigmoid','dtanh')
grid on





figure(2)
x = 0:0.01:10;
y1 = 10*tanh(x);
y2 = tanh(0.5 * x);

plot(x,y1,'b',...
      'LineWidth',2,...
       'MarkerSize',5,...
       'MarkerEdgeColor','r',...
       'MarkerFaceColor',[0.5,0.5,0.5])
hold on 
grid on
plot(x,y2,'r',...
      'LineWidth',2,...
       'MarkerSize',5,...
       'MarkerEdgeColor','r',...
       'MarkerFaceColor',[0.5,0.5,0.5])
legend('y1','y2')
grid on

