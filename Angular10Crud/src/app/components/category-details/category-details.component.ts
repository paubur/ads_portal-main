import { Component, OnInit } from '@angular/core';
import { CategoryService } from 'src/app/services/category.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-category-details',
  templateUrl: './category-details.component.html',
  styleUrls: ['./category-details.component.css']
})
export class CategoryDetailsComponent implements OnInit {
  currentCategory = null;
  message = '';

  constructor(
    private categoryService: CategoryService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.message = '';
    this.getCategory(this.route.snapshot.paramMap.get('id'));
  }

  getCategory(id): void {
    this.categoryService.get(id)
      .subscribe(
        data => {
          this.currentCategory = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  updateCategory(): void {
    this.categoryService.update(this.currentCategory.id, this.currentCategory)
      .subscribe(
        response => {
          console.log(response);
          this.message = 'The tutorial was updated successfully!';
        },
        error => {
          console.log(error);
        });
  }

  deleteCategory(): void {
    this.categoryService.delete(this.currentCategory.id)
      .subscribe(
        response => {
          console.log(response);
          this.router.navigate(['/category/']);
        },
        error => {
          console.log(error);
        });
  }
}
