    is_defined = function (value) {
        return typeof(value) !== 'undefined' && value !== null
    };

    function getBooksName()
    {
        answers = [];
        var variant_mass = document.getElementsByName('var');
        for (var i = 0; i < variant_mass.length; i++)
        {
            if (variant_mass[i].checked)
            {
                var ca = answers[i];
                if(!is_defined(ca))
                {
                    answers.push(variant_mass[i].value);
                }
            }
        }

        console.log(answers);
        return answers
    }
    function sendBooksName()
    {
        var resultBooksName = getBooksName()[0];
       alert(getBooksName()[0]);
        return getBooksName()[0]
    }