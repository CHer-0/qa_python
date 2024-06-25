# test methods. The coll_fill function helps you create a test collector and fill it with the books you need for the test from dictionary.

  # add_new_book
    # +positive
      test_add_new_book_add_two_books
      test_add_new_book_add_extremal_len_name
    # -negative
      test_add_new_book_add_over_extremal_len_name

  # set_book_genre
    # +positive
      test_genre_not_empty
      test_set_book_genre_set_genre_in_list
    # -negative
      test_set_book_genre_set_genre_not_in_list

  # get_book_genre
    # +positive
      test_get_book_genre_exist_book
    # -negative
      test_get_book_genre_not_exist_book

  # get_books_with_specific_genre
    # +positive
      test_get_books_with_specific_genre_two_exist_book_genre
    # -negative
      test_get_books_with_specific_genre_not_book_genre

  # get_books_genre
    # +positive
      test_get_books_genre_return_dict

  # get_books_for_children
    # +positive
      test_get_books_for_children_two_books_for_children
    # -negative
      test_get_books_for_children_two_books_not_for_children

  # add_book_in_favorites
    # +positive
      test_add_book_in_favorites_two_exist_books
    # -negative
      test_add_book_in_favorites_two_not_exist_books
    
  # delete_book_from_favorites
    # +positive
      test_delete_book_from_favoritess_two_exist_books
    # -negative
      test_delete_book_from_favoritess_two_not_exist_books

  # get_list_of_favorites_books
    # +positive
      test_get_list_of_favorites_books_return_list
	  