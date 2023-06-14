function button_click_kid_gnrt() {
    var theme_select = document.getElementById( '1_dropbox');
    var theme = theme_select.options[theme_select.selectedIndex].value;
    document.getElementById('butt_generate').innerHTML="Вы ввели : "+ theme;
}

$('#theme_one').submit(function(){

	alert('Нажата submit-кнопка');

	return false;
});