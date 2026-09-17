# Forecast
This is Forecast. A little application made to help start your day. 

Background
When i wake up in the morning... if I wake up... I'm always rushing to find my tiny phone, check my calendar, get dressed, and then comeback in because it's too hot for a hoodie
So, why not re purpose my TV in the mornings. It's a huge screen in my room AND it probably isn't dead in the morning unlike my phone.

Thought process
Here is the link to the High Level System design made on draw.io:                                                                                                                                                                                                                                                        
https://drive.google.com/file/d/1q0CnNIEm5DfHwpEylwfCtQw1M9rowYPO/view?usp=sharing

The program needs to turn on when i wake up, hence we can turn on a TV via HDMI CEC. Meaning loading a program on a low power Single board computer, and using it to display information at a set time.

Access to today's weather forecast can be pulled from multiple free weather API's such as https://www.weatherapi.com/. and today's itinart can be pulled directly from subscription/public calenders.

putting these together, forecast can temporarily hijack my TV to tell me my timetable and the weather, replacing the need to mess around with my phone (which is usaually dead), and it can do this in the morning and right before bedtime.
