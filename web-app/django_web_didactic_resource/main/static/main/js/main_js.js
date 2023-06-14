          var count_create_db = 1;

          function count_create_db_inc(){
            this.count_create_db = count_create_db + 1;
          }

          function count_create_db_dec(){
            this.count_create_db = count_create_db - 1;
          }

          function get_count_create_db(){return count_create_db;}

          function viewDivTwo(){
            document.getElementById("choose_theme_two").style.display = "flex";
            document.getElementById("button__add-topic-One").style.display = "none";
            document.getElementById("button__add-topic-Two").style.display = "block";
            document.getElementById("button__delete-topic-Two").style.display = "block";
            count_create_db_inc();
          };

          function viewDivThree(){
            document.getElementById("choose_theme_three").style.display = "flex";
            document.getElementById("button__add-topic-Two").style.display = "none";
            document.getElementById("button__add-topic-Three").style.display = 'block';

            document.getElementById("button__delete-topic-Two").style.display = 'none';
            document.getElementById("button__delete-topic-Three").style.display = 'block';
            count_create_db_inc();
          };

          function viewDivFour(){
            document.getElementById("choose_theme_four").style.display = "flex";
            document.getElementById("button__add-topic-Three").style.display = "none";
            document.getElementById("button__delete-topic-Three").style.display = "none";
            document.getElementById("button__delete-topic-Four").style.display = "block";
            count_create_db_inc();
          };

          function viewDeleteTwo(){
            document.getElementById("choose_theme_two").style.display = "none";
            document.getElementById("button__add-topic-Three").style.display = "none";
            document.getElementById("button__add-topic-One").style.display = "block";
            document.getElementById("button__add-topic-Two").style.display = "none";
            document.getElementById("button__delete-topic-Two").style.display = 'none';
            count_create_db_dec();
          };

          function viewDeleteThree(){
            document.getElementById("choose_theme_three").style.display = "none";
            document.getElementById("button__add-topic-Three").style.display = "none";
            document.getElementById("button__delete-topic-Three").style.display = 'none';
            document.getElementById("button__add-topic-Two").style.display = "block";
            document.getElementById("button__delete-topic-Two").style.display = 'block';
            count_create_db_dec();
          };

          function viewDeleteFour(){
            document.getElementById("choose_theme_four").style.display = "none";
            document.getElementById("button__delete-topic-Four").style.display = 'none';
            document.getElementById("button__add-topic-Three").style.display = "block";
            document.getElementById("button__delete-topic-Three").style.display = 'block';
            count_create_db_dec();
          };

          function button_click_generate() {
                    var site_mapping = new Map();

                    var count_var = document.getElementById('task_options_area').value;
                    if (count_var != "" && document.getElementById('input_FIO_area').value != ""){
                        alert("Выберите что-то одно из общего задания и индивидуального");
                        return;
                    }
                    if (count_var != ""){
                        site_mapping.set('count_var', count_var);
                    }
                    else if (document.getElementById('input_FIO_area').value != ""){
                        var FIO = document.getElementById('input_FIO_area').value;
                        site_mapping.set('FIO', FIO);
                    }
                    else{
                        alert("Вы забыли заполнить поля ФИО/Кол-во вариантов");
                        return;
                    }
                    var iter = get_count_create_db();
                    var i = 1;
                    while(i <= iter){
                        var i_str = String(i);
                        var theme_select = document.getElementById(i_str + '_dropbox');
                        var theme = theme_select.options[theme_select.selectedIndex].value;
//                        alert(document.getElementById('input_count_tasks_'+ i_str).value != "");
                        if (document.getElementById('input_count_tasks_'+ i_str).value != "")
                        {
                            var count_task = document.getElementById('input_count_tasks_'+ i_str).value;
                        }
                        else {
                            alert("Введите необходимое количество задач.");
                            return;
                        }
                        site_mapping.set(theme, count_task);
                        i = i + 1;
                    }

                    button_print.onsubmit = async (e) => {
                    e.preventDefault();

                    let response = await fetch('/article/formdata/post/user', {
                      method: 'POST',
                      body: new FormData(formElem)
                    });

                    let result = await response.json();

                    alert(result.message);
                  };
//                    $.ajax({
//                      type: "POST",
//                      url: "/generated_tasks",
//                      data: site_mapping,
//                      success: function (result) {
//                         alert("Отправил");
//                      },
//                      dataType: "json"
//                    });
//                    $.ajax({
//                      type: "GET",
//                      url: "http://127.0.0.1:8000/photo/click_on_photo/",
//                      data: icon.dataset.counter,
//                      dataType: "text",
//                      cache: false,
//                      success: function(data) {
//                        loadComments(data)
//                      }
//                    var theme_first_select = document.getElementById('first_dropbox');
//                    theme_first = theme_first_select.options[theme_first_select.selectedIndex].value;
//                    site_mapping.set('first_dropbox', theme_first);
//                    alert(document.getElementById("button__add-topic-Two").style.display == "flex");
//                    document.getElementById('butt_generate').innerHTML="Вы ввели : "+ site_mapping.get('4_dropbox');
//                      site_mapping.forEach((value, key) => alert(key +" " + value));
//)
                };