import { Component, OnInit } from '@angular/core';
import { CategoryService } from 'src/app/services/category.service';

@Component({
  selector: 'app-category-list',
  templateUrl: './category-list.component.html',
  styleUrls: ['./category-list.component.css']
})
export class CategoryListComponent implements OnInit {

  category: any;
  currentCategory = null;
  currentIndex = -1;
  name = '';

  constructor(private categoryService: CategoryService) { }

  ngOnInit(): void {
    this.retrieveCategory();
  }


  retrieveCategory(): void {
    this.categoryService.getAll()
      .subscribe(
        data => {
          this.category = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.retrieveCategory();
    this.currentCategory = null;
    this.currentIndex = -1;
  }

  setActiveCategory(category, index): void {
    this.currentCategory = category;
    this.currentIndex = index;
  }

  removeAllCategory(): void {
    this.categoryService.deleteAll()
      .subscribe(
        response => {
          console.log(response);
          this.retrieveCategory();
        },
        error => {
          console.log(error);
        });
  }

}
